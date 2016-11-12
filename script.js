$(document).ready(function(){
  const qs = getQueryString(location.search)
  console.log(qs)
  $('#input-text').text(qs.inputText)
  $('#output-text').text(qs.outputText)
})

function getQueryString(str) {
  const result = {}
  str = str.slice(1)
  const arr = str.split('&')
  
  arr.forEach(function(item) {
    result[item.split('=')[0]] = item.split('=')[1]
  })
  
  return result
}
