from __future__ import print_function

### ========
# Interfaces
### ========

class Transaction(object):
    """ Command interface. """
    def execute(self):
        raise NotImplementedError("Execute method not yet implemented.")

### =============
# Implementations
### =============

class SELECT(Transaction):
    """ Concrete SELECT Command. """
    def __init__(self, transaction):
        self.transaction = transaction

    def execute(self):
        self.transaction.SELECT()

class INSERT(Transaction):
    """ Concrete INSERT Command. """
    def __init__(self, transaction):
        self.transaction = transaction

    def execute(self):
        self.transaction.INSERT()

class UPDATE(Transaction):
    """ Concrete UPDATE Command. """
    def __init__(self, transaction):
        self.transaction = transaction

    def execute(self):
        self.transaction.UPDATE()


class TransactionManager(object):
    """ Receiver object. """

    def SELECT(self):
        print("Performing SELECT operation!")

    def INSERT(self):
        print("Performing INSERT operation!")

    def UPDATE(self):
        print("Performing UPDATE operation!")


class TransactionBroker(object):
    """ Invoker object. """

    def __init__(self):
        self.__transaction_queue = []

    def request_transaction(self, transaction):
        """ Add a transaction/command to the queue. """

        self.__transaction_queue.append(transaction)

    def execute_transaction_queue(self):
        """ Execute all transactions in queue. """

        for t in self.__transaction_queue:
            print("...executing command in queue...")
            t.execute()


def main():
    # Set up the receiver
    transaction = TransactionManager()

    # Set up commands
    tr_select = SELECT(transaction)
    tr_insert = INSERT(transaction)
    tr_update = UPDATE(transaction)

    # Set up the invoker
    broker = TransactionBroker()

    # Make request for commands
    broker.request_transaction(tr_select)
    broker.request_transaction(tr_insert)
    broker.request_transaction(tr_select)
    broker.request_transaction(tr_insert)
    broker.request_transaction(tr_update)
    broker.request_transaction(tr_update)

    # Execute commands
    broker.execute_transaction_queue()

if __name__ == '__main__':
    main()