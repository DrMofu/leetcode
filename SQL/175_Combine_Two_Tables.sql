SELECT Person.lastName, Person.firstName, Address.city, Address.state
FROM Person
LEFT JOIN Address
ON Person.personID=Address.personID;