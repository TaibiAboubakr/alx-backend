#!/usr/bin/node
// 0-redis_client.js
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.connect().catch((err) => {
  console.error(`Error connecting to Redis: ${err.message}`);
});
