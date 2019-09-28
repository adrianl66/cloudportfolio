import React from 'react';
import ReactDom from 'react-dom';
import ExampleWork from './example-work.js';

const myWork = [
  {
    'title': "Work Example",
    'href': "https://example.com",
    'desc': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, " +
              "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " +
              "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " +
              "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in " +
              "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " +
              "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa " +
              "qui officia deserunt mollit anim id est laborum.",
    'image': {
      'desc': "example screenshot of a project involving code",
      'src': "images/example1.png",
      'comment': "",
    },
  },
  {
    'title': "Text Translation",
    'href': "https://example.com",
    'desc': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, " +
              "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " +
              "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " +
              "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in " +
              "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " +
              "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa " +
              "qui officia deserunt mollit anim id est laborum.",
    'image': {
      'desc': "example screenshot of a project involving chemistry",
      'src': "images/example2.png",
      'comment': `“Chemistry” by Surian Soosay is licensed under CC BY 2.0
           https://www.flickr.com/photos/ssoosay/4097410999`,
    },
  },

  {
    'title': "IOT",
    'href': "https://example.com",
    'desc': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, " +
              "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " +
              "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " +
              "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in " +
              "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " +
              "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa " +
              "qui officia deserunt mollit anim id est laborum.",
    'image': {
      'desc': "Temperature/Humidity sensors by Location",
      'src': "images/example3.png",
      'comment': `“Bengal cat” by roberto shabs is licensed under CC BY 2.0
           https://www.flickr.com/photos/37287295@N00/2540855181`,
    },
  },
];

ReactDom.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
