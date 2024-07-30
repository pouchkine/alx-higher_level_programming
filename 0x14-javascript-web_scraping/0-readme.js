#!/usr/bin/node

const fs = require('fs');

function readAndPrintFile (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error(`Error reading file: ${error.message}`);
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <file_path>');
} else {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
}
