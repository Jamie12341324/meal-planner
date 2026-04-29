
function button_click_(e){
    alert("button_click " + e.srcElement.id);
}
// tests if a input is a number and says "That is not a number" if its not
// validate numeric input from stackoverflow
function isNum(p){
    if (isNaN(p.value)){
        alert("That is not a number");
        p.value="";
        p.focus();
    }
}
// checks to see if there is the same fruit already there when you click the add food button and adds the fruit if it is not there
function button_click(e){
    let buttons=document.getElementsByClassName("btn-success");
    this_id = e.srcElement.id;
    for (let i=0; i<buttons.length; i++){
                let things_in_meal=document.getElementById("in_meal");
                let food=buttons[i].id.substr(3,buttons[i].id.length);
                //alert(food);
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
                    // inserting a tag after another from w3schools
                if (this_id == buttons[i].id ) reference.after(para);
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
            }
            }
// deletes fruit from list of fruits to add
function button_click2(e){
            // information on substr function found on w3schools
            this_id = e.srcElement.id.substring(3,e.srcElement.id.length);
            let buttons2=document.getElementsByClassName("btn-danger");
            for (let i2=0; i2<buttons2.length; i2++){
              let food2=buttons2[i2].id.substring(3,buttons2[i2].id.length);
              if (this_id == buttons2[i2].id.substring(3,buttons2[i2].id.length) ) {
                    deleted=document.getElementById(food2);
                    deleted.remove();
              }
            }
        }

document.addEventListener("DOMContentLoaded", function(){
    let button1=document.getElementById("meal_name_button");
    // checks to see if a meal already has the same name as the one you are trying to create and blocks it if its the same
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
    });
    // does the same thing as button1 but need to come from a seperate id because there are two examples of almost the same button but 
    // only one appears at a time because one is rename meal and the other is create meal
    let button1b=document.getElementById("meal_name_buttonb");
    if (button1b){
        button1b.addEventListener("click", function(){
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
        });
    }
    // checks to see if there is the same fruit already there when you click the add food button and adds the fruit if it is not there
    let buttons=document.getElementsByClassName("btn-success");
    for (let i=0; i<buttons.length; i++){
            if (buttons[i].id!="meal_name_button"){
                buttons[i].addEventListener("click", button_click );
        }
    }
    // deletes fruit from list of fruits to add
    let buttons2=document.getElementsByClassName("btn-danger");
    for (let i2=0; i2<buttons2.length; i2++){
        buttons2[i2].addEventListener("click",button_click2);
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
    return _new;
}
