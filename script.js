$(document).ready(function(){
  const qs = getQueryString(location.search)

  if (qs.inputText) {
    $('#input-text').text(decodeURI(qs.inputText))
  }

  if (qs.outputText) {
    $('#output-text').text(decodeURI(qs.outputText))
  }

  $('#form').on('submit', function(e) {
    e.preventDefault()

    $.ajax({
      method: 'POST',
      url: '/verarbeitet',
      data: {
        eingabe: encodeURI($('#input-text').val())
      }
    })
  })
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
