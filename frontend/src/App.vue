<script lang="ts">
import {defineComponent} from 'vue'
import ChessBoard, {type Board, Piece} from "@/components/ChessBoard.vue";

export default defineComponent({
  name: "App",
  components: {ChessBoard},
  data: () => {
    return {
      board: [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        [null, null, null, null, null, null, null, null],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
      ] as Board
    }
  }
})
</script>

<template>
  <ChessBoard :board="board"></ChessBoard>
</template>

<style scoped>
#app {
  min-height: 100vh;
}
</style>