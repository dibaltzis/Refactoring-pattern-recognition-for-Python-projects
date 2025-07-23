[◀️ back to main page](../../README.md)
### Criteria/Steps

- Find variable declarations that are class fields (like class B from v1 and the field var_y).
- Check if the class to which the field belongs is not a superclass. Class B has a superclass A.
- Check in the same variable in the second version if it starts with "super().__init__(" (class B from v2).
- Check if the superclass of class B from v1 does not contain the field.
- Check if there are more than one subclass with the same field and compare with the corresponding classes in the second version for the existence of this (class B and class C).
- Check in version 2 of the file if the same field (var_y) does not exist in the subclasses (class B and class C from v2) with their same superclass (class A from v2).
- Check for the existence of the initial field (var_y from class B of v1) in the superclass of the second version (class A from v2).

### Κριτήρια/βήματα

- Εύρεση ορισμών μεταβλητών (variable declaration) οι οποιοί είναι πεδία κλάσης (ως class B από v1 και το πεδίο var_y).
- Έλεγχος για το αν η κλάση που ανήκει το πεδίο δεν είναι υπέρ κλάση.Η class B εχει υπερκλάση την class A.
- Έλεγχος στην ίδια μεταβλητή στην δεύτερη έκδοση αν ξεκινάει με “super().__init__(“ (class B από v2).
- Έλεγχος αν η υπερ κλάση της class B από v1 δεν περιέχει το πεδίο.
- Έλεγχος αν υπάρχουν παραπάνω από μια υποκλάση με το ίδιο πεδίο και σύγκριση με τις αντίστοιχες κλάσεις της δεύτερης έκδοση για την ύπαρξη αυτού (class B και class C).
- Έλεγχος στην έκδοση 2 του αρχείου αν δεν υπάρχει το ίδιο πεδίο( var_y) στις υποκλάσεις(class B και class C από ν2) με την ίδια υπερκλάση τους (class A από ν2). 
- Έλεγχος για την ύπαρξη του αρχικού πεδίου (var_y από class B της v1) στην υπερκλάση της δεύτερης έκδοσής(class A από ν2).
