-- trigger to decrease item qty
DELIMITER //
CREATE TRIGGER DecreaseItemQuantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the item quantity in the items table based on the order
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_id = NEW.item_id;
END;
//
DELIMITER ;
