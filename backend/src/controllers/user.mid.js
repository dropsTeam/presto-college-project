const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken")
const User = require('../models/user.model');
const Admin = require("../models/admin.model")


// Middleware for verifying the token before letting user visit any page...

// verify token whenever admin adds/delete amount....
const verifyToken = async (req, res, next)=> {
 //check header or url parameters or post parameters for token
// ? If you have a bearer token
//  var token = req.headers['authorization'].split(" ")[1];
 var token = req.headers['authorization'];
 console.log(token)
 if (!token) {
   return res.status(403).send({ auth: false, message : 'User not Authenticated' });
 }
 //verifies secret and checks exp
 else{
  await jwt.verify(token, "secret124", function(err, decoded) {      
    if (err) {
      return res.status(500).send({ auth: false, message: 'Failed to Authenticate token.' });    
    }
    //if everything is good, save to request for use in other routes
    req.userId = decoded.id;
    next();
  });
 }
}


// testing middleware : use howsoever you want :)
const main = (req,res) =>{
  res.send(res.locals.password)
}


// register route...
const registerUser = async (req,res) =>{
 await User.findOne({email:req.body.email},async (err,docs)=>{ 

  if(err){
   res.status(401).send(
    'Error occured !'
   );
  } 

  else if(docs){
   res.status(401).send("User already exists!!!");
   // res.redirect("/api/user");
  }

  else{
   try{
     let user = new User(req.body)

      await user.save((err,user)=>{
        if (err) return res.status(500).send("There was a problem registering the user "+err);
        // if user is registered without errors
        // create a token
        else if(!err){
          var token = jwt.sign({ id: user._id }, "kitten", {
            expiresIn: 10 // expires in 24 hours
          });
          console.log("user has been created")
          res.send({token:token,userid : user._id})
        } 
      });
    }
     catch(err){
       res.status(401).send("User already exists!!!");
    }
   }

 })
}



// login route....
const loginUser = (req,res) =>{
  
  console.log(req.body)

  const query = { email : req.body.email};
  let password = req.body.password ;
  //jas will manually add a password and we will compare that password while logging in...
 
    User.findOne(query, async function(err, user) {
        if (err) { 
          return res.status(401).send({
            error: 'Error in finding User !.'
           });
         }
        if (!user) {
          console.log('Username not Found, Please Register !')
           return res.status(401).send('Username not found')
         }
        else{
          try{
            // todo : we will add this later when we have an encrypted password at backend.....
            // if( await bcrypt.compare(password,res.locals.password)){
              if(password == res.locals.password){
                  // if password also correct then -----
                  var token = jwt.sign({ id: user._id }, "secret124", {
                    expiresIn: 3600 * 24// expires in 24 hours
                   });
                  console.log("logged in !!!"+ token)
                  res.send({token:token,user : user})
                  // else
                }else{
                   res.status(401).send('Incorrect Password');
                }
            }catch(err){
              console.log(err)
              res.status(401).send({
                error: 'Error occured!!!'
             });
           }
        }
      }
    )
  };
  



  
  //  get all users registered
  const getUsers = async(req,res)=>{
    try{
      await User.find((err,docs)=>{
        if(err){
          res.status(401).send("error occured in finding user")
        }
        else{
          res.send(docs);
        }
      })
    }
    catch(err){
      if(err){
        res.status(401).send(err)
      }
    }
  }



  // route : delete user...
   const deleteUser = async (req,res) =>{
    // get the query filter
      let query = {'_id': req.params.id};
  
      await User.findOneAndRemove(query,(err,docs)=>{
        if(err){
          res.status(401).send("error occured in deleting user")
        }
        else{
          console.log("deleted")
          res.send(docs);
        }
      })
    }


  // route to edit user :
  const editUser = async (req,res) =>{
    const filter = { _id : req.params.id };
    const update = req.body;

     await User.findOneAndUpdate(filter, update, {
      new: true
     },(err,docs)=>{
       if(err){
        res.status(401).send("error occured in updating user")
       }
       else{
        console.log("updated")
        res.send(docs);
       }
    });
  }



  // add funds into logged in accounts
  const addFunds = async(req,res) =>{
    // this is the logged user id comming from the verifyToken middleware while checking it:
    let query = {_id:req.userId}

    await User.findOneAndUpdate(
     query,
      { $inc: { amount: req.body.amount/2 }},
      (err,docs)=>{
        if(err){
          res.status(401).send("error occured in updating amount")
          }
        else{
          console.log("amount added : "+req.body.amount)
          res.send(docs);
          }
        }
     )
  }



  // remove funds from looged in accounts
  const removeFunds = async(req,res) =>{
    // this is the logged user id comming from the verifyToken middleware while checking it:
    let query = {_id:req.userId}

    await User.findOneAndUpdate(
     query,
      { $inc: { amount: -(req.body.amount/2) }},
      (err,docs)=>{
        if(err){
          res.status(401).send("error occured in removing amount")
          }
        else{
          console.log("amount removed: "+req.body.amount)
          res.send(docs);
          }
        }
     )
  }



// todo: later tasks for admin section
  // add a new admin
  const addAdmin = async (req,res) =>{
    await Admin.findOne({email:req.body.email},async (err,docs)=>{ 
   
     if(err){
      res.status(401).send(
       'Error occured !'
      );
     } 
   
     else if(docs){
      res.status(401).send("Admin already exists!!!");
      // res.redirect("/api/user");
     }
   
     else{
      try{
        let admin = new Admin(req.body)
   
         await admin.save((err,admin)=>{
           if (err) return res.status(500).send("There was a problem registering a new admin "+err);
           // if user is registered without errors
           // create a token
           else if(!err){
             console.log("admin has been created")
             res.send(admin)
           } 
         });
       }
        catch(err){
          res.status(401).send("Admin already exists!!!");
       }
      }
   
    })
   }


module.exports = {main ,verifyToken, registerUser ,loginUser ,getUsers, deleteUser ,editUser , addFunds, removeFunds, addAdmin};