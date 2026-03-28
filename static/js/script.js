document.addEventListener("DOMContentLoaded", function(){
    let buttons=document.getElementsByClassName("btn-success");
    console.log("hello");
    for (let i=0; i<buttons.length; i++){
        buttons[i].addEventListener("click", function(){
            things_in_meal=document.getElementById("in_meal");
            let food=buttons[i].id;
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
                para.innerText=food;
                let reference=things_in_meal.children[0];
                things_in_meal.insertBefore(para,reference);
            }
        });
    }
});
