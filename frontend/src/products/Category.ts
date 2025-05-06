export class Category {
  id: string | null = "";
  name: string | null = null;
  description: string | null = null;

  constructor(initializer?: {
    id: string | null;
    name: string | null;
    description: string | null;
  }) {
    if (!initializer) return;
    if (initializer.id) this.id = initializer.id;
    if (initializer.name) this.name = initializer.name;
    if (initializer.description) this.description = initializer.description;
  }
}
