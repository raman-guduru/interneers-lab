export class Product {
  id: string = "";
  name: string = "";
  description: string | null = null;
  brand: string = "";
  price: number | null = null;
  quantity: number | null = null;

  constructor(initializer?: {
    id: string;
    name: string;
    description: string | null;
    brand: string;
    price: number | null;
    quantity: number | null;
  }) {
    if (!initializer) return;
    if (initializer.id) this.id = initializer.id;
    if (initializer.name) this.name = initializer.name;
    if (initializer.description) this.description = initializer.description;
    if (initializer.brand) this.brand = initializer.brand;
    if (initializer.price) this.price = initializer.price;
    if (initializer.quantity) this.quantity = initializer.quantity;
  }
}
