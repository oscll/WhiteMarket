<template>
<div class="container h-100">
    <div class="row">
         <div class="col-md-10 offset-md-1">
                    <span class="anchor" id="formComplex"></span>
                    <hr class="my-5">
                    <h3>Complex Form Example </h3>
                    
                    <!-- form complex example -->
                    <div class="form-row mt-4">
                        <div class="col-sm-5 pb-3">
                            <label for="productTitle">Title</label>
                            <input type="text" class="form-control" id="productTitle" placeholder="WhiteMarket Product !!!">
                        </div>
                        <div class="col-sm-3 pb-3">
                        </div>
                        <div class="col-sm-4 pb-3">
                            <label for="productAmount">Amount</label>
                            <div class="input-group">
                                <div class="input-group-prepend"><span class="input-group-text">$</span></div>
                                <input type="decimal" class="form-control" id="productAmount" placeholder="616.11">
                            </div>
                        </div>
                        <div class="col-sm-6 pb-3">
                            <label for="">First Name</label>
                            <input type="text" class="form-control" id="exampleFirst">
                        </div>
                        <div class="col-sm-6 pb-3">
                            <label for="exampleLast">Last Name</label>
                            <input type="text" class="form-control" id="exampleLast">
                        </div>
                        <div class="col-sm-6 pb-3">
                            <label for="exampleCity">City</label>
                            <input type="text" class="form-control" id="exampleCity">
                        </div>
                        <div class="col-sm-3 pb-3">
                            <label for="exampleSt">State</label>
                            <select class="form-control" id="exampleSt">
                                <option>Pick a state</option>
                            </select>
                        </div>
                        <div class="col-sm-3 pb-3">
                            <label for="exampleZip">Postal Code</label>
                            <input type="text" class="form-control" id="exampleZip">
                        </div>
                        <div class="col-md-6 pb-3">
                            <label for="exampleAccount">Color</label>
                            <div class="form-group small">
                                <div class="form-check form-check-inline">
                                    <label class="form-check-label">
                                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1"> Blue
                                    </label>
                                </div>
                                <div class="form-check form-check-inline">
                                    <label class="form-check-label">
                                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2"> Red
                                    </label>
                                </div>
                                <div class="form-check form-check-inline disabled">
                                    <label class="form-check-label">
                                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio3" value="option3" disabled=""> Green
                                    </label>
                                </div>
                                <div class="form-check form-check-inline">
                                    <label class="form-check-label">
                                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option4"> Yellow
                                    </label>
                                </div>
                                <div class="form-check form-check-inline">
                                    <label class="form-check-label">
                                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option5"> Black
                                    </label>
                                </div>
                                <div class="form-check form-check-inline">
                                    <label class="form-check-label">
                                        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option6"> Orange
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 pb-3">
                            <label for="exampleMessage">Message</label>
                            <textarea class="form-control" id="exampleMessage"></textarea>
                            <small class="text-info">
                              Add the packaging note here.
                            </small>
                        </div>
                        <div class="col-12">
                            <div class="form-row">
                                 <label class="col-md col-form-label"  for="name">Generated Id</label>
                                 <input type="text" class="form-control col-md-4" name="gid" id="gid" />
                                 <label class="col-md col-form-label"  for="name">Date Assigned</label>
                                 <input type="text" class="form-control col-md-4" name="da" id="da" />
                            </div>
                        </div>
                        <div class="col-md-12 pb-3">
                            <label for="exampleMessage">Message</label>
                            <textarea class="form-control" id="exampleMessage"></textarea>
                            <small class="text-info">
                              Add the packaging note here.
                            </small>
                        </div>
                    </div>

                </div>
    </div>
</div>
</template>

<script>
/* import { GET_PRODUCTS, } from '@/store/modules/products'
export default {

  computed: {
    products() {
      return this.$store.getters.products
    }
  },
  methods: {
    date(date){
      let validDate = date.split('.')[0]
      let diference = new Date() - new Date(validDate)

      switch (true) {
        case (diference/1000) > 0 && (diference/1000) < 60  :
            return `Hace ${Math.round(diference/1000)} segundos.`
          break;
        case ((diference/1000)/60) > 0 && ((diference/1000)/60) < 60  :
            return `Hace ${Math.round((diference/1000)/60)} minutes.`
          break;
        case (((diference/1000)/60)/60) > 0 && (((diference/1000)/60)/60) < 60  :
            return `Hace ${Math.round(((diference/1000)/60)/60)} hours.`
          break;
        case ((((diference/1000)/60)/60)/24) > 0 && ((((diference/1000)/60)/60)/24) < 7  :
            return `Hace ${Math.round((((diference/1000)/60)/60)/24)} days.`
          break;
        case (((((diference/1000)/60)/60)/24)/7) > 0 && (((((diference/1000)/60)/60)/24)/7) < 13  :
            return `Hace ${Math.round(((((diference/1000)/60)/60)/24)/7)} weeks.`
          break;

        default:
            return `Hace mucho tiempo ${data.getFullYear()}-${date.getMonth()}-${date.getDate()}`
          break;
      }

      return date; 
    }
  },
  beforeCreate: function(){
    this.$store.dispatch(GET_PRODUCTS)
  }
}; */
</script>

<style lang="scss" scoped>
.card{ 
  min-width: 32.552083333333336vw !important;
}
</style>
