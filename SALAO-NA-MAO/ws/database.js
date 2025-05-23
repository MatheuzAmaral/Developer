const mongoose = require('mongoose');

const URI = 'mongodb+srv://pro1canaldomt:<db_password>@clusterdev.lul0oy5.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDev';

const env = process.env.NODE_ENV || 'dev';
let options = {};

mongoose.set('useNewUrlParser', true);
mongoose.set('useFindAndModify', false);
mongoose.set('useCreateIndex', true);
mongoose.set('useUnifiedTopology', true);

mongoose
  .connect(URI, options)
  .then(() => console.log('DB is Up!'))
  .catch((err) => console.log(err));
