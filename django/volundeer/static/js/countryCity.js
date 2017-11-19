var countries = new Array();

states['Romania'] = new Array('Timisoara','Bucuresti', 'Cluj', 'Iasi', 'Brasov', 'Sibiu', 'Ianca');
states['United Kingdom'] = new Array('London', 'Manchester', 'Chelsea', 'Liverpool', 'Birmingham');


function setCities() {
  cntrySel = document.getElementById('country');
  cityList = cities[cntrySel.value];
  changeSelect('city', cityList);
}
function changeSelect(fieldID, newOptions, newValues) {
  selectField = document.getElementById(fieldID);
  selectField.options.length = 0;
  for (i=0; i<newOptions.length; i++) {
    selectField.options[selectField.length] = new Option(newOptions[i], newValues[i]);
  }