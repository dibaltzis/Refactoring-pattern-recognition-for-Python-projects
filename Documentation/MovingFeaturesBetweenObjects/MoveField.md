[◀️ back to main page](../../README.md)
### Criteria/Steps

- Find classes in the code lines of the first version of the file and their fields (as class A from v1).
- Find the same class (from the first version) in the second version of the file and its fields (as class A from v2).
- Compare the fields of the two classes.
- Find each different field within some other class in the file of the second version (as class B from v2).
- Check the correlation of the class to which the different field of the first class belongs (class A and class B v2). The correlation concerns whether one is a subclass or superclass of the other.
- Check if the field of class B v2 exists in the same class of the first version, class B v1.

### Κριτήρια/βήματα

- Εύρεση κλάσεων στις  γραμμές κώδικα της πρώτης έκδοσης του αρχείου και των πεδίων αυτών(ως class A από v1).
- Εύρεση της ίδιας κλάσης (της πρώτης έκδοσης) στην δεύτερη έκδοση του αρχείου και των πεδίων αυτής(ως class A από v2).
- Σύγκριση των πεδίων των δύο κλάσεων.
- Εύρεση κάθε διαφορετικού πεδίου εντός κάποιας άλλης κλάσης στο αρχείο της δεύτερης έκδοσης (ως class B από v2).
- Έλεγχος της συσχέτισης της κλάσης που βρέθηκε να ανήκει το διαφορετικό πεδίο της πρώτης κλάσης(class A και class B  v2). Η συσχέτιση αφορά αν είναι  υπο ή υπερ κλάση η μια της άλλης. 
- Έλεγχος του πεδίου της κλάσης  class B  v2 αν υπάρχει στην ίδια κλάση της πρώτης έκδοσης class B  v1.



file 1  | file 2
------- | -------
class A | class A
x,y     | y
class B |class B
z       | x,z