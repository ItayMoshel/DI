// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}

funcOne()
// The initial value of 'a' is 5, but it's updated to 3 within the if block.

// #1.2
// With 'const', you would get a syntax error because you can't reassign a constant variable.

//#2
let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1
funcThree()
funcTwo();
funcThree();
// Initially, 'a' is set to 0. After 'funcTwo' is called, 'a' is updated to 5.

// #2.2
// With 'const', you would get a syntax error when trying to reassign 'a' in funcTwo because constants can't be reassigned.

//#3
function funcFour() {
    window.a = "hello";
}

function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1
funcFour();
funcFive();
// 'funcFour' assigns the value "hello" to the global variable 'a', which is accessible in 'funcFive'.

//#4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}

// #4.1
funcSix();
// The local variable 'a' within 'funcSix' shadows the outer 'a', so the inner 'a' ("test") is used.

// #4.2
// Nothing significant would change since 'a' is already being declared in the function's scope.

//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);
// The inner 'a' within the if block has scope limited to that block. 
// Outside the if block, the outer 'a' is used.

// #5.1
// in the if block 5
// outside of the if block 2

// #5.2
// The same behavior would occur, The inner 'a' would shadow the outer one within the if block.
