a=document.body.innerHTML;
m=a.match(/(data:image[^\\\"]+)/g);
m.pop(); // fails on last one for some reason
for (var i=0; i<m.length; i++) {
  var download = document.createElement('a');
  download.href = m[i];
  download.download = 'portrait'+i+'.jpg';
  download.click();
}
