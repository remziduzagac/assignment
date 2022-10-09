DROP TABLE IF EXISTS `listing`;

CREATE TABLE `listing` (
	`id` INT NOT NULL,
	`address` VARCHAR(512) DEFAULT NULL,
	`price` DOUBLE,
	PRIMARY KEY (`id`)
);

INSERT INTO listing (id,address,price) VALUES (
  '0',
  '7312 Lancaster Rd. Noblesville, IN 46060',
  '950000');

INSERT INTO listing (id,address,price) VALUES (
  '1',
  '245 Prospect Ave. New Lenox, IL 60451',
  '250000');

INSERT INTO listing (id,address,price) VALUES (
  '2',
  '9157 Annadale St. Augusta, GA 30906',
  '350000');

INSERT INTO listing (id,address,price) VALUES (
  '3',
  '51 Oak Valley St. Westfield, MA 01085',
  '350000');

INSERT INTO listing (id,address,price) VALUES (
  '4',
  '266 Selby Drive Severn, MD 21144',
  '350000');

INSERT INTO listing (id,address,price) VALUES (
  '5',
  '9956 Tallwood Street North Haven, CT 06473',
  '370000');

INSERT INTO listing (id,address,price) VALUES (
  '6',
  '35 3rd Rd. Upland, CA 91784',
  '150000');

INSERT INTO listing (id,address,price) VALUES (
  '7',
  '150 S. Westport Ave. Palm City, FL 34990',
  '470000');

INSERT INTO listing (id,address,price) VALUES (
  '8',
  '774 Valley View Dr. Land O Lakes, FL 34639',
  '850000');

INSERT INTO listing (id,address,price) VALUES (
  '9',
  '40 Lyme St. Smithtown, NY 11787',
  '750000');

INSERT INTO listing (id,address,price) VALUES (
  '10',
  '305 West Elizabeth St. Milwaukee, WI 53204',
  '650000');

SELECT * FROM listing;