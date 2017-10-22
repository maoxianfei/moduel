
//开始循环
var start=setInterval(
function() {
if(Date.now() >= new Date("2017-08-16 15:59:30")) {
document.querySelector('#J_flash > ul.sale-col2.container.clearfix > li:nth-child(6) > div > div.con-r > a').click();//立即领取
}
},10);

//结束循环
clearInterval(start);


var start=function(){
for (var i=0;i<5;i++){
$('#sub_content').val(i); 
$('#checking_data').click();
$('#alert_error > div.popbox > div.popbtn > a').click();
alert('2');
}
}.call();