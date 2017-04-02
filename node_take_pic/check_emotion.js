var oxford = require('project-oxford')
var client = new oxford.Client('7426de5456344bab95321c97e5bf3a57')
var fs = require('fs')
var iter = 0

function max(response) {

}

fs.watchFile('image0.jpg', (curr, prev) => {
  client.emotion.analyzeEmotion({
    path: 'image0.jpg',
  }).then(function (response) {
	try {      
	if(response.length > 0)
	  {
		fs.createReadStream('image0.jpg').pipe(fs.createWriteStream('faces/image'+iter++ +'.jpg')); 
	  }
	else fs.createReadStream('image0.jpg').pipe(fs.createWriteStream('others/image'+iter++ +'.jpg'));
	console.log(response)
	}
	catch(error){
	console.log(error)
	}	
  }).catch(function(error) {
    console.log(error)
  })
  console.log(`the current mtime is: ${curr.mtime}`);
  console.log(`the previous mtime was: ${prev.mtime}`);
})
