#@app.route('/')
#def list_users():
    """Shows list of all users in db"""
 #   users = User.query.all()
  #  return redirect("/users")
 #   #return render_template('list.html', users=users)

 """Show users main page"""    
@app.route('/users')
  def users_index():  
    users = User.query.all()
    return render_template('users/index.html', users=users)

  Post(db.Model):

    tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.Text,
                     nullclass Pable=False)                     

    content = db.Column(db.Text,
                     nullable=False)  

    created_at = db.Column(
                db.DateTime,
                nullable=False,
                default=datetime.datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  

    @property
    def friendly_date(self):
        return self.createa_at.strftime("%a %b %-d %Y, %-I:%M %p")                   
                     
