#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (const i = 0; i < x; i++) {
  console.log('X'.repeat(x));
		    }
}
