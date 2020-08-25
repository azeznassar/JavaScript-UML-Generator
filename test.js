class Cat {
    constructor(catName, catAge) {
      this.catName = "test-string";
      this.catAge = 0;
    }
    
    speak() {
      console.log(`${this.catName} makes a noise.`);
    }

    displayAge() {
      console.log(`${this.catName} is ${this.catAge}.`);
    }
}

class Dog {
  constructor(dogName, dogAge) {
    this.dogName = dogName;
    this.dogAge = dogAge;
  }
  
  speak() {
    console.log(`${this.dogName} makes a noise.`);
  }

  displayAge() {
    console.log(`${this.dogName} is ${this.dogAge}.`);
  }
}