function login(){
   var userName=$("#uName").val();
   var userPass=$("#uPass").val();
   if(userName==""||userName==null){
   	alert("用户名不能为空")
   	return false;
   }
else if (userPass==""||userPass==null){
	alert("密码不能为空")
	return false;
}else 
{
	return true;
}
}
