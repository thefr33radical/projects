<?php
	
	  ini_set('display_errors',1);
	  require_once('db_config.php'); 	
	  
	  $dbh=mysql_connect
	  (
		$db['default']['hostname'],
		$db['default']['username'],
		$db['default']['password'])
		or die('Cannot connect to the database because: ' . mysql_error());
		mysql_select_db ($db['default']['database']);

		
	$result = array('status'=>false);
	$input_data = json_decode(trim(file_get_contents('php://input')), true);
					
	$purchase_card_number = $input_data["purchase_card_number"];
	$purchase_name_on_Card = $input_data["purchase_name_on_Card"];
	$purchase_expiry_date = $input_data["purchase_expiry_date"];
	$purchase_card_cvv = $input_data["purchase_card_cvv"];
	$purchase_card_pin = $input_data["purchase_card_pin"];
	$bank_name = $input_data["bank_name"];
	$purchase_merchant_name = "IRIDIUM";
	$user_type = "user";
	$product_bought = $input_data["product_bought"];
	
	
	$dbsql = "INSERT INTO transaction_details (sl_num, customer_name, customer_id, merchant_name, merchant_id, user_type, product, bank_name, card_number, card_name, expiry_date, card_cvv, card_pin) VALUES (null, '".$purchase_name_on_Card."', 1, '".$purchase_merchant_name."', 1 , '".$user_type."', '".$product_bought."', '".$bank_name."', '".$purchase_card_number."', '".$purchase_name_on_Card."', '".$purchase_expiry_date."', '".$purchase_card_cvv."', '".$purchase_card_pin."')";

	$index_id = 0;
	mysql_query(trim($dbsql)) or print(mysql_error()); 
	$index_id = mysql_insert_id($dbh);
	
	$result['id'] = $index_id;
	echo json_encode($result,true);
	exit();
	
?>