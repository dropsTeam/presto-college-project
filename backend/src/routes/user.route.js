const route = require('express').Router();
const userController = require('../controllers/user.mid');
const { verifyToken } = require('../controllers/user.mid');


route.post("/register",userController.registerUser)

route.post("/login",userController.loginUser)

route.get("/getUsers",userController.getUsers)

route.delete("/delete/:id",userController.verifyToken, userController.deleteUser)

route.put("/edit/:id",userController.verifyToken, userController.editUser)

route.post('/addFunds',userController.verifyToken,userController.addFunds)
route.post("/removeFunds",userController.verifyToken,userController.removeFunds)

route.get("/main",userController.main)


module.exports = route;