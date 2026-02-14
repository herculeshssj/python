<template>
  <div>
    <h1>Itens da API</h1>
    <ul>
      <li v-for="item in items" :key="item">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ItemList",
  data() {
    return { items: [] };
  },
  mounted() {
    fetch("http://127.0.0.1:8000/items")
      .then(res => res.json())
      .then(data => { this.items = data.items; })
      .catch(err => console.error("Erro:", err));
  }
};
</script>
