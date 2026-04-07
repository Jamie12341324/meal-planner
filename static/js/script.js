document.addEventListener("DOMContentLoaded", function(){
    let buttons=document.getElementsByClassName("btn-success");
    console.log("hello");
    for (let i=0; i<buttons.length; i++){
        buttons[i].addEventListener("click", function(){
            let things_in_meal=document.getElementById("in_meal");
            let food=buttons[i].innerText;
            let c=0;
            let L=things_in_meal.children.length;
            var _new=true;
            while (c<L){
                if (food===things_in_meal.children[c].innerText){
                    _new=false;
                }
                c=c+1;
            }
            if (_new===true){
                let para=document.createElement("p");
                para.innerText=buttons[i].id.substr(3,buttons[i].id.length);
                para.id=buttons[i].id.substr(3,buttons[i].id.length);
                let reference=things_in_meal.children[0];
                reference.after(para);
                let textarea = document.createElement("textarea");
                textarea.name="example";
                textarea.innerText=buttons[i].id.substr(3,buttons[i].id.length);
                textarea.style.display="none";
                para.appendChild(textarea);
            }
        });
    }
    let buttons2=document.getElementsByClassName("btn-danger");
    for (let i2=0; i2<buttons2.length; i2++){
        buttons2[i2].addEventListener("click",function(){
            // information on substr function found on w3schools
            let food2=buttons2[i2].id.substr(3,buttons2[i2].id.length);
            alert(food2);
            _new=search(food2);
            if (_new!==true){
                deleted=document.getElementById(food2);
                deleted.remove();
            }
        });
    }
});
function search(food){
    let things_in_meal=document.getElementById("in_meal");
    let c=0;
    let L=things_in_meal.children.length;
    var _new=true;
    while (c<L){
        if (food===things_in_meal.children[c].innerText){
            _new=c;
        }
        c=c+1;
    }
    return _new
}
