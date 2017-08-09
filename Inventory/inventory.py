lockedItemTypes = set()
itemTypes = ('widget', 'gadget')
itemNum = {
    'widget': 99,
    'gadget': 99
    }

class Inventory:
    num = 0
    global lockedItemTypes
    global itemTypes
    global itemNum
    def lock(self, item_type):
        '''Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different
        customers.'''
        if item_type not in itemTypes:
            raise InvalidItemType(item_type)
        elif item_type not in lockedItemTypes:
            lockedItemTypes.add(item_type)
        else:
            raise InUse(item_type)

    def unlock(self, item_type):
        '''Release the given type so that other
        customers can access it.'''
        if item_type not in itemTypes:
            raise InvalidItemType(item_type)
        else:
            lockedItemTypes.remove(item_type)

    def purchase(self, item_type):
        '''If the item is not locked, raise an
        exception. If the item_type does not exist,
        raise an exception. If the item is currently
        out of stock, raise an exception. If the item
        is available, subtract one item and return
        the number of items left.'''
        global lockedItemTypes
        if item_type not in itemTypes:
            raise InvalidItemType(item_type)
        elif item_type not in lockedItemTypes:
            raise Unlock(item_type)
        else:
            return  itemNum[item_type] - 1


class InvalidItemType(Exception):
    def __init__(self, item_type):
        super().__init__("Sorry, we don't sell {}".format(item_type))
        self.item_type = item_type


class InUse(Exception):
    def __init__(self, item_type):
        super().__init__("Item type {} is in use".format(item_type))
        self.item_type = item_type


class Unlock(Exception):
    def __init__(self, item_type):
        super().__init__("Item type {} hasn't been locked".format(item_type))
        self.item_type = item_type

item_type = 'widget'
inv = Inventory()
inv.lock(item_type)
try:
    num_left = inv.purchase('wdget')
except InvalidItemType as e:
    print("Sorry, we don't sell {}".format(item_type))
else:
    print("Purchase complete. There are "
          "{} {}s left".format(num_left, item_type))
finally:
    inv.unlock(item_type)
