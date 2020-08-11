const mongoose = require('mongoose');
const types = mongoose.Schema.Types;

// user model
const userSchema = mongoose.Schema({
  timeStamp: {
    type: types.Date,
    default: Date.now
  },
  name:{
   type:types.String,
   required:true
 },
 email:{
   type:types.String,
   required:true
 },
 phone:{
   type: Number,
   required:true
 },
 dob:{
   type:String,
   required:true
 },
 imageUrl:{
  type:String
 },
 address:{
   street : {
      type:types.String,
      maxlength: 100,
      default: ''
     },
   city:{ 
     type:types.String,
     maxlength :30,
     default :''
   } ,
   state:{
     type:types.String,
     maxlength :5,
     default : ''
   },
   zipCode :{
     type:types.Number,
     default:""
   }   
 },
 amount:{
   type:types.Number,
   default:0
 }
})



module.exports = mongoose.model('newusers', userSchema);
