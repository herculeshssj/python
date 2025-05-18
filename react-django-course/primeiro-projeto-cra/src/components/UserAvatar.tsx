export const UserAvatar = () => {
  return (
    <>
        <div className="flex items-center">
        <img
            src="https://via.placeholder.com/150"
            alt="User Avatar"
            className="w-10 h-10 rounded-full"
            onClick={() => alert('User Avatar Clicked')}
        />
        <span className="ml-2 text-sm font-medium">John Doe</span>
        </div>
    </>
  );
}