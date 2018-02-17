module.exports = {
  'QAWorks Contact Us' : function (browser) {
    browser
      .useXpath()
      .url('http://www.qaworks.com/contact-us/')
      // .waitForElementVisible('body', 10000)
      .setValue('//input[@name="your-name"]', 'j.Bloggs')
      .setValue('//input[@name="your-email"]', 'j.Bloggs@qaworks.com')
      .setValue('//input[@name="your-company"]', 'test automation')
      .setValue('//textarea[@name="your-message"]', 'please contact me I want to find out more')
      .click('//input[@id="contact-us-send"]')
      .pause(1000)
      // .assert.containsText('#main', 'Night Watch')
      .end();
  }
};
