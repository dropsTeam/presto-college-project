const mongoose = require("mongoose");

const db =  process.env.MONGODB_URI || 'mongodb+srv://jashan:jashan123@cluster0.huicb.mongodb.net/<dbname>?retryWrites=true&w=majority';

// mongoose.Promise = global.Promise;

// function to connect to database....
const ConnectDB = async () =>{
 try{
   await mongoose.connect(db,{
    useNewUrlParser:true,
    useUnifiedTopology:true
   })
   console.log("Connected to MongoDB Database")
 }catch(err){
   if(err){
    console.log("Error occured while connecting")
    process.exit(1);
   }
 }
}

module.exports = ConnectDB;

