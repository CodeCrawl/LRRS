DELIMITER $$
CREATE PROCEDURE `sp_current_inactive_bookings` ()
BEGIN
select * from bookings 
where	booking_status = 'NS' and 
			ssp_current_inactive_bookingstart_date >= current_date() and 
            start_time >= timediff(current_time(), '00:15:00');
END$$
DELIMITER ;

