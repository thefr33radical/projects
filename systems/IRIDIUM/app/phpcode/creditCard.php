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
				   
	$credit_card_number = $input_data["credit_card_number"];
	$credit_card_type = $input_data["credit_card_type"];
	$credit_card_bank_name = $input_data["credit_card_bank_name"];
	$credit_card_exp_date = $input_data["credit_card_exp_date"];
	$credit_card_cvv = $input_data["credit_card_cvv"];
	$credit_card_pin = $input_data["credit_card_pin"];
	$card_id = $credit_card_bank_name . "01";
	$customerName = "gowtham";
			
		
	$dbsql = "INSERT INTO cards (card_number, card_type, cvv, pin, expiry_date, card_sl_num, cards_id, bank_name, customer_id, name) VALUES ('".$credit_card_number."', '".$credit_card_type."', '".$credit_card_cvv."', '".$credit_card_pin."', '".$credit_card_exp_date."', null , '".$card_id."', '".$credit_card_bank_name."', 1, '".$customerName."')";

	$index_id = 0;
	mysql_query(trim($dbsql)) or print(mysql_error()); 
	$index_id = mysql_insert_id($dbh);
	
	$result['id'] = $index_id;
	echo json_encode($result,true);
	exit();
	
?>