document.addEventListener("DOMContentLoaded", function(){
    let button1=document.getElementById("meal_name_button");
    button1.addEventListener("click", function(){
        let names=document.getElementsByClassName("meal_names");
        let current_name=document.getElementById("meal_name");
        let i3=0;
        while (i3<names.length){
            // .value from Bing AI
            if (names[i3].innerText==current_name.value){
                alert("There is already a meal with that name pick a different name");
            }
            i3=i3+1;
        }
    })
    let buttons=document.getElementsByClassName("btn-success");
    console.log("hello");
    for (let i=0; i<buttons.length; i++){
            buttons[i].addEventListener("click", function(){
            let things_in_meal=document.getElementById("in_meal");
            let food=buttons[i].id.substr(3,buttons[i].id.length);;
            alert(food)
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
                // information on how to use substr from w3schools
                para.innerText=buttons[i].id.substr(3,buttons[i].id.length);
                para.id=buttons[i].id.substr(3,buttons[i].id.length);
                let reference=things_in_meal.children[0];
                // inserting a tag after antoher from w3schools
                reference.after(para);
                // information used to pick textarea for holding information on foods from w3schools
                let textarea = document.createElement("textarea");
                // adding a name to a textarea put inside a p tag from AI so that all the food types can get used by the view
                // to save the items to the database because textareas have a attribute of .name
                textarea.name="example";
                // information on how to use substr from w3schools
                textarea.innerText=buttons[i].id.substr(3,buttons[i].id.length);
                textarea.style.display="none";
                // appendChild from w3schools
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
                // information on how to delete elements from mdn
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
