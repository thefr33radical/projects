<?php
	
	  ini_set('display_errors',1);
	  require_once('db_config.php'); 	
	  
	  /* echo '<pre>';
		 print_r($db['default']);
	  echo '</pre>'; */

	  //echo 'Trying to connect to database: ' .$db['default']['database'];
	  $dbh=mysql_connect
	  (
		$db['default']['hostname'],
		$db['default']['username'],
		$db['default']['password'])
		or die('Cannot connect to the database because: ' . mysql_error());
		mysql_select_db ($db['default']['database']);

	  //echo '<br />   Connected OK:'  ;

		
	$result = array('status'=>false);
	$input_data = json_decode(trim(file_get_contents('php://input')), true);
	
	$bank_user_name = $input_data["bank_user_name"];
	$bank_password = $input_data["bank_password"];
	$bank_branch = $input_data["bank_branch"];
	$bank_city = $input_data["bank_city"];
	$bank_pin_code = $input_data["bank_pin_code"];
	$bank_state = $input_data["bank_state"];
	$bank_balance = $input_data["bank_balance"];
	$bank_name = $input_data["bank_name"];
	$bankId = $bank_name ."001";
	$bank_type = "private";
	$bank_ifsc_code = $bank_name."IFSC111";
	
	$dbsql = "INSERT INTO bank_acc (sl_num, bank_id, busername, bpassword, bankname, branch, city, pincode, state, banktype, cust_balance, ifsc_code, username, usertype) VALUES (null, '".$bankId."', '".$bank_user_name."', '".$bank_password."', '".$bank_name."', '".$bank_branch."', '".$bank_city."', '".$bank_pin_code."', '".$bank_state."', '".$bank_type."', '".$bank_balance."', '".$bank_ifsc_code."', '', '')";

	$index_id = 0;
	mysql_query(trim($dbsql)) or print(mysql_error()); 
	$index_id = mysql_insert_id($dbh);
	
	$result['id'] = $index_id;
	echo json_encode($result,true);
	exit();
	
?>