<script lang="ts">
import {defineComponent, type PropType} from "vue";

type Piece = 'k' | 'q' | 'r' | 'b' | 'n' | 'p' | 'K' | 'Q' | 'R' | 'B' | 'N' | 'P'

type BoardSquare = Piece | null;
type Board = BoardSquare[][];

export default defineComponent({
  name: 'ChessBoard',
  props: {
    board: {
      type: Array as PropType<Board>,
      required: true,
    },
  },
})
</script>

<template>
  <div class="chessboard">
    <div v-for="(row, rowIndex) in board" :key="rowIndex" class="row">
      <div
          v-for="(piece, columnIndex) in row"
          :key="`${columnIndex}-${rowIndex}`"
          :class="[
              (columnIndex + rowIndex) % 2 == 0 ? 'black' : 'white',
              'square',
          ]"
      >
        <img
            :src="`src/assets/pieces/${piece}.svg`"
            alt=""
            v-if="piece"
            :class="['piece']"
            draggable="true"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.chessboard {
  width: 400px;
  height: 400px;
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  grid-template-rows: repeat(8, 1fr);
}

.row {
  display: contents;
}

.square {
  height: 100%;
  width: 100%;
  background-color: red;
  display: flex;
  align-items: center;
  justify-content: center;
}

.square.white {
  background-color: #f0d9b5;
}

.square.black {
  background-color: #b58863;
}

.piece {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
