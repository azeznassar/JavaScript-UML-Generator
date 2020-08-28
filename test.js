class Cat {
    constructor(catName, catAge) {
      this.catName = "";
      this.catAge = true;
    }
    
    speak(words) {
      console.log(`${this.catName} wants to say: ${words}`);
      dog = new Dog("Name", 123)

      return 34
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

    return "MyString"
  }

  displayAge() {
    console.log(`${this.dogName} is ${this.dogAge}.`);
  }
}