const mongoose = require('mongoose');
const types = mongoose.Schema.Types;

// user model
const adminSchema = mongoose.Schema({
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
 }
})



module.exports = mongoose.model('admin', adminSchema);