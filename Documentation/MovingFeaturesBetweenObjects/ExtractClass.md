[◀️ back to main page](../../README.md)
### Criteria/Steps

- Find the classes in the code lines of the second version of the file (as class B v2) that belong to the list of newly introduced classes.
- Find the fields in the constructor of this class (class B v2).
- Find the classes in the file of the first version that correspond to those in the second version (as class A v1 and class A v2 for the second version).
- Find the fields in the constructor of this class (class A v1) and compare these fields with the fields of class B v2. The purpose of the comparison is to find common fields.
- Check for the existence of the common field in class A v2

### Κριτήρια/βήματα

- Εύρεση κλάσεων στις  γραμμές κώδικα της δεύτερης έκδοσης του αρχείου(ως class B  v2) που ανήκουν στη λίστα με τις νεοεισαχθείς κλάσεις. 
- Εύρεση των πεδίων στον κονστράκτορα της κλάσης αυτής (class B  v2).
- Εύρεση κλάσεων στο αρχείο της πρώτης έκδοσης οι οποίες αντιστοιχούν με αυτές της δεύτερης (ως class A  v1 και class A  v2 για την δεύτερη έκδοση).
- Εύρεση των πεδίων στον κονστράκτορα της κλάσης αυτής (class Α  v1) και σύγκριση των πεδίων αυτών με τα πεδία της  class B  v2. Ο σκοπός της σύγκρισης ειναι η εύρεση κοινών πεδίων.
- Έλεγχος για την ύπαρξη του κοινού πεδίου στη class A  v2

file 1          |   file 2
----------------| -------------
class A         | class A
    self.x      |   self.x
    self.y      |   self.y    
    self.z      |
                | class B
                |   self z
            