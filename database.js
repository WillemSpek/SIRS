db.employees.insertMany([
  {ID: 'clarkkent1', name: 'Clark', surname: 'Kent', salary: 90000, absence: 3, parental: 6, overtime: 9},
  {ID: 'borisjohn2', name: 'Boris', surname: 'John', salary: 45000, absence: 9, parental: 3, overtime: 6}
]);

db.engineering.insertMany([
  ,
  {ID: 'borisjohn2', name: 'Boris', salary: 45000, authorisation: ['bla bla'], production: ['management'], status: 'on payed leave'}
]);

db.externals.insertMany([
  {ID: 'chips3', name: 'chiphard', provider: 'thing', type: 'chips', tax: 4.5},
  {ID: 'GPU1', name: 'Nvidio', provider: 'other thing', type: 'gpus', tax: 6.6}
]);


db.employees.find({name: 'Clark'});
