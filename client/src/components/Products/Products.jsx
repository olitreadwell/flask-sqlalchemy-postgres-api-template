import { useState, useEffect } from "react";

const Products = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const getProducts = async () => {
      const url = "http://localhost:5555/api/v1/products";
      const response = await fetch(url);
      let json = await response.json();
      let products = json;
      setProducts(products);
    };

    getProducts();
  }, []);

  return (
    <section>
      <h1>Products</h1>
      <ul>
        {products.map((product) => (
          <li key={`${product.id}-${product.name}`}>
            <p>{product.id}</p>
            <p>{product.name}</p>
            <p>{product.category}</p>
            <p>{product.price}</p>
            <p>{product.quantity}</p>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default Products;
