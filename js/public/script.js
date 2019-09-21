// document.getElementById('comment_text').innerText = `
// import sys
// fptr = open(sys.argv[1],'r')
// a = fptr.readline()
// print(a)
// `;

function getdata()
{
    var a = document.getElementById('comment_text')
    var b = document.getElementById('stdin')
    // var a = document.getElementById('editorContainer')

    
console.log(a.value)
console.log(b.value)
axios({
    method: 'POST',
    url: 'http://localhost:3000/runit',
    data: {
      "textit": a.value,
      "stdin":b.value
    }
  }).then(function(response) {
    console.log(response.data);
    var store = ''+response.data
    var storeagain = store.replace("[H[2J","")
    console.log(storeagain)

    document.getElementById('terminal_text').value = storeagain;
  });
  
  
// axios.get('http://localhost:3000/runit/'+a.value)
//   .then(function(response){
//     console.log(response.data); 
//     console.log(response.status); 
//   });  
    
}
// $(document).ready(function() {
//   $(".editable").keydown(function(e) {  
//       switch(e.which) {
          
//           case 219: //open curly bracket
//                       console.log(e.which)
//                       document.getElementById('comment_text').value += '{}';
//                       // this.value = '}';
//               break;
//           case 188: //less than
//                   this.value += '>';
//               break;
//           }
//       });
//   })
var editorContainer = document.querySelector('.editorContainer')
CodeMirror(editorContainer, {
  lineNumbers: true,
  mode: 'javascript',
  value: 'var b = 3;'
})