[◀️ back to main page](../../README.md)
### Criteria/Steps

- Finding variable declarations that are class fields (as class A from v1 and the field var_y).
- Checking if the class to which the field belongs is a superclass.
- Checking the corresponding line of code in the second version if the field (var_y) does not exist. This checks if the field does not exist in the second version of the file.
- Checking in the subclasses of class A from v1 if the field is contained in the form "super().__init__(".
- Checking in the subclasses of class A from v2 if the field is contained not in the form "super().__init__(" but in its regular form.

### Κριτήρια/βήματα

- Εύρεση ορισμών μεταβλητών (variable declaration) οι οποίοι είναι πεδία κλάσης (ως class Α από v1 και το πεδίο var_y).
- Έλεγχος για το αν η κλάση που ανήκει το πεδίο είναι υπέρ κλάση.
- Έλεγχος της αντίστοιχης γραμμής κώδικα της δεύτερης έκδοσης αν δεν υπάρχει το πεδίο(var_y).Πραγματοποιείται δηλαδή έλεγχος αν το πεδίο δεν υπάρχει στη δεύτερη έκδοση του αρχειου.
- Έλεγχος στις υποκλάσεις της class A από ν1 αν περιέχεται το πεδίο με την μορφή “super().__init__(“ .
- Έλεγχος στις υποκλάσεις της class A από ν2 αν περιέχεται το πεδίο,  όχι με την μορφή “super().__init__(“ αλλά με την κανονική μορφή του.
