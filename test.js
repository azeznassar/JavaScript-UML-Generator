class Cat {
    constructor(catName, catAge) {
      this.catName = "";
      this.catAge = "";
    }
    
    speak() {
      console.log(`${this.catName} makes a noise.`);
      dog = new Dog("Name", 123)
    }

    displayAge() {
      console.log(`${this.catName} is ${this.catAge}.`);
    }
}

class Dog {
  constructor(dogName, dogAge) {
    this.dogName = "test-string";
    this.dogAge = 0;
  }
  
  speak() {
    console.log(`${this.dogName} makes a noise.`);
  }

  displayAge() {
    console.log(`${this.dogName} is ${this.dogAge}.`);
  }
}