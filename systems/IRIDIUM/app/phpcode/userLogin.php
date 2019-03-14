<?php
	
      $result = array('status'=>false);	
	  ini_set('display_errors',1);
	  require_once('db_config.php'); 	
	 
	  //echo 'Trying to connect to database: ' .$db['default']['database'];
	  $dbh=mysql_connect
	  (
		$db['default']['hostname'],
		$db['default']['username'],
		$db['default']['password'])
		or die('Cannot connect to the database because: ' . mysql_error());
		mysql_select_db ($db['default']['database']);
		
	$result = array('status'=>false);
	$input_data = json_decode(trim(file_get_contents('php://input')), true);
	
	$user_name = $input_data["user_name"];
	$user_password = $input_data["user_password"];
	
	$dbsql = "select * from user_login_master where username = '".$user_name."' and password = '".$user_password."' ";
	
	if (mysql_num_rows($dbsql) >0) {
		$result['status'] = 'true';
	}
	
	echo json_encode($result,true);
	exit();
	
?>