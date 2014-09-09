test('um mictorio vazio', function() {
  equal(proximoMictorio([vazio]), 0);
});

test('dois mictorios vazios', function() {
  equal(proximoMictorio([vazio, vazio]), 0);
});

test('primeiro ocupado e o segundo vazio; ', function() {
  equal(proximoMictorio([ocupado, vazio]), 1);
});

test('primeiro ocupado com três mictorios', function() {
  equal(proximoMictorio([ocupado, vazio, vazio]), 2);
});
