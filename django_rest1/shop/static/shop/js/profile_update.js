fetch('https://domain.com/api/update', {
  method: 'PUT',
  body: JSON.stringify({
    id: 1,
    product: 'apple',
    category: 'fruit',
  }),
  headers: {
    'Content-Type': 'application/json',
  },
})
  .then((res) => res.json())
  .then((data) => console.log(data))
  .catch((err) => console.error(err));