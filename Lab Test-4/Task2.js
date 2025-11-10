// /c:/Users/DEEKSHA/Desktop/AIAC/Lab Test-4/Task2(1).js

// JavaScript object equivalent of the Python dictionary
const studentInfo = {
    name: "John",
    age: 20,
    grades: [85, 90, 92],
};

// Object operations
console.log("Original object:", studentInfo);

// Accessing values
console.log("Name:", studentInfo.name);
console.log("Age:", studentInfo.age);

// Adding a new key-value pair
studentInfo.course = "Computer Science";
console.log("After adding course:", studentInfo);

// Modifying a value
studentInfo.age = 21;
console.log("After modifying age:", studentInfo);

// Removing a key-value pair
delete studentInfo.grades;
console.log("After deleting grades:", studentInfo);

// Checking if key exists
if ("name" in studentInfo) {
    console.log("Name exists in object");
}

// Getting all keys and values
console.log("Keys:", Object.keys(studentInfo));
console.log("Values:", Object.values(studentInfo));