const express = require("express")
const bodyParser = require('body-parser')
const fs = require('fs');
const execSync = require('child_process').execSync;




const app = express()
app.use(express.static('public'))
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({  limit: '50mb',extended: true, parameterLimit:50000, }));

app.set('view engine','pug')
app.get('/',(req,res)=>{
  res.render('index')
})
app.post('/runit',(req,res)=>{
  // console.log(req.body)
  fs.writeFile('input.txt', req.body.stdin, function (err) {
  fs.writeFile('here.py', req.body.textit, function (err) {
    if (err) throw err;
    try {
      let output = execSync('clear && python3 here.py input.txt', { encoding: 'utf-8' })
      res.json(output)
  } catch(err) {
    res.json(err.message.toString().replace('Command failed: clear && python3 here.py',' ').replace('File "here.py",',''))
  }
});
});
// fs.writeFile('mahesh.c', req.body.textit, function (err) {
//   if (err) throw err;
//   try {
//     let output = execSync('clear && gcc -o hello mahesh.c && ./hello', { encoding: 'utf-8' })
//     res.json(output)
// } catch(err) {
//   res.json(err.message.toString().replace('Command failed: clear && python3 here.py',' ').replace('File "here.py",',''))
// }
// });
  
  // fs.writeFile('here.js', req.body.textit, function (err) {
  //   if (err) throw err;
  //   let output = execSync('clear && node here', { encoding: 'utf-8' });
  //   res.json(output);
    
  // });
})

app.listen(3000)